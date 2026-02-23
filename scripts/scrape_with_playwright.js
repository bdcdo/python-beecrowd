const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const problems = JSON.parse(fs.readFileSync('/home/brunodcdo/Desktop/dev/2026/23_URI/problems_list.json', 'utf8'));
const dir = '/home/brunodcdo/Desktop/dev/2026/23_URI/beecrowd_iniciante';

if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

function sanitizeName(name) {
  return name.toLowerCase()
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-z0-9]+/g, '_')
    .replace(/^_|_$/g, '');
}

function buildMarkdown(id, name, subject, level, data) {
  let md = `# ${id} - ${name}\n\n`;
  md += `**Categoria:** Iniciante\n`;
  md += `**Assunto:** ${subject}\n`;
  md += `**Nível:** ${level}\n`;
  if (data.author) md += `**Autor:** ${data.author}\n`;
  if (data.timelimit) md += `**${data.timelimit}**\n`;
  md += `\n---\n\n`;

  if (data.descText) {
    md += `## Descrição\n\n${data.descText}\n\n`;
  }

  if (data.inputText) {
    md += `## Entrada\n\n${data.inputText}\n\n`;
  }

  if (data.outputText) {
    md += `## Saída\n\n${data.outputText}\n\n`;
  }

  if (data.examples && data.examples.length > 0) {
    data.examples.forEach((ex, i) => {
      const label = data.examples.length > 1 ? ` ${i + 1}` : '';
      md += `## Exemplo de Entrada${label}\n\n\`\`\`\n${ex.input}\n\`\`\`\n\n`;
      md += `## Exemplo de Saída${label}\n\n\`\`\`\n${ex.output}\n\`\`\`\n\n`;
    });
  }

  return md;
}

async function extractProblem(page) {
  return await page.evaluate(() => {
    const header = document.querySelector('.header');
    const problem = document.querySelector('.problem');

    if (!header && !problem) {
      return { error: 'No problem content found' };
    }

    const author = header?.querySelector('p')?.textContent?.trim() || '';
    const timelimit = header?.querySelector('strong')?.textContent?.trim() || '';
    const title = header?.querySelector('h1')?.textContent?.trim() || '';

    const descDiv = problem?.querySelector('.description');
    const descText = descDiv ? descDiv.innerText.trim() : '';

    const inputDiv = problem?.querySelector('.input');
    const inputText = inputDiv ? inputDiv.innerText.trim() : '';

    const outputDiv = problem?.querySelector('.output');
    const outputText = outputDiv ? outputDiv.innerText.trim() : '';

    const tables = problem?.querySelectorAll('table');
    const examples = [];
    tables?.forEach(table => {
      const rows = table.querySelectorAll('tbody tr');
      rows.forEach(row => {
        const cells = row.querySelectorAll('td');
        if (cells.length >= 2) {
          examples.push({
            input: cells[0].innerText.trim(),
            output: cells[1].innerText.trim()
          });
        }
      });
    });

    return { title, author, timelimit, descText, inputText, outputText, examples };
  });
}

async function main() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
  });
  const page = await context.newPage();

  let processed = 0;
  let skipped = 0;
  const failed = [];

  for (let i = 0; i < problems.length; i++) {
    const p = problems[i];
    const filename = `${p.id}_${sanitizeName(p.name)}.md`;
    const filepath = path.join(dir, filename);

    // Skip if already exists and has content (>200 bytes)
    if (fs.existsSync(filepath)) {
      const stat = fs.statSync(filepath);
      if (stat.size > 200) {
        skipped++;
        processed++;
        if (processed % 50 === 0) console.log(`Progress: ${processed}/${problems.length} (skipped ${skipped})`);
        continue;
      }
    }

    try {
      const url = `https://resources.beecrowd.com/repository/UOJ_${p.id}.html`;
      await page.goto(url, { timeout: 30000, waitUntil: 'domcontentloaded' });

      // Wait for either the problem content or a Cloudflare challenge
      await page.waitForSelector('.problem, .description, h1, .main-content', { timeout: 15000 }).catch(() => {});

      // Check if we hit Cloudflare challenge
      const isChallenge = await page.evaluate(() => {
        return document.title.includes('Just a moment') || document.title.includes('Attention Required');
      });

      if (isChallenge) {
        // Wait for Cloudflare to resolve
        console.log(`  Cloudflare challenge for ${p.id}, waiting...`);
        await page.waitForSelector('.problem, .description, h1', { timeout: 30000 });
      }

      const data = await extractProblem(page);

      if (data.error) {
        failed.push({ id: p.id, error: data.error });
        console.error(`  Failed ${p.id}: ${data.error}`);
        continue;
      }

      const md = buildMarkdown(p.id, p.name, p.subject, p.level, data);
      fs.writeFileSync(filepath, md, 'utf8');
      processed++;

      if (processed % 25 === 0) {
        console.log(`Progress: ${processed}/${problems.length} (skipped ${skipped})`);
      }
    } catch (err) {
      failed.push({ id: p.id, error: err.message.substring(0, 200) });
      console.error(`  Failed ${p.id}: ${err.message.substring(0, 100)}`);
    }
  }

  await browser.close();

  console.log(`\nDone! Processed: ${processed}, Skipped: ${skipped}, Failed: ${failed.length}`);
  if (failed.length > 0) {
    console.log('Failed IDs:', failed.map(f => f.id).join(', '));
    fs.writeFileSync(path.join(dir, '_failed.json'), JSON.stringify(failed, null, 2), 'utf8');
  }
}

main().catch(console.error);
