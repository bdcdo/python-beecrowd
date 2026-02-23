const fs = require('fs');
const path = require('path');
const https = require('https');

const problems = JSON.parse(fs.readFileSync('/home/brunodcdo/Desktop/dev/2026/23_URI/problems_list.json', 'utf8'));
const dir = '/home/brunodcdo/Desktop/dev/2026/23_URI/beecrowd_iniciante';

if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

function sanitizeName(name) {
  return name.toLowerCase()
    .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-z0-9]+/g, '_')
    .replace(/^_|_$/g, '');
}

function fetchURL(url) {
  return new Promise((resolve, reject) => {
    https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0' } }, (res) => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        return fetchURL(res.headers.location).then(resolve).catch(reject);
      }
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve(data));
      res.on('error', reject);
    }).on('error', reject);
  });
}

function stripHtml(html) {
  return html
    .replace(/<img[^>]*>/g, '')
    .replace(/<br\s*\/?>/gi, '\n')
    .replace(/<\/p>/gi, '\n')
    .replace(/<p[^>]*>/gi, '')
    .replace(/<strong>/gi, '**').replace(/<\/strong>/gi, '**')
    .replace(/<em>/gi, '*').replace(/<\/em>/gi, '*')
    .replace(/<sub>/gi, '').replace(/<\/sub>/gi, '')
    .replace(/<sup>/gi, '^').replace(/<\/sup>/gi, '')
    .replace(/<[^>]+>/g, '')
    .replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&')
    .replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&nbsp;/g, ' ')
    .replace(/&iacute;/g, 'í').replace(/&aacute;/g, 'á').replace(/&eacute;/g, 'é')
    .replace(/&oacute;/g, 'ó').replace(/&uacute;/g, 'ú').replace(/&atilde;/g, 'ã')
    .replace(/&otilde;/g, 'õ').replace(/&ccedil;/g, 'ç').replace(/&agrave;/g, 'à')
    .replace(/&ecirc;/g, 'ê').replace(/&ocirc;/g, 'ô').replace(/&uuml;/g, 'ü')
    .replace(/&#\d+;/g, '')
    .replace(/\n{3,}/g, '\n\n')
    .trim();
}

function parseHTML(html) {
  const result = { author: '', timelimit: '', descText: '', inputText: '', outputText: '', examples: [] };

  const authorMatch = html.match(/<div class="header">[\s\S]*?<p>([\s\S]*?)<\/p>/);
  if (authorMatch) {
    result.author = authorMatch[1].replace(/<[^>]+>/g, '').trim();
  }

  const tlMatch = html.match(/<strong>(Timelimit:[\s\S]*?)<\/strong>/);
  if (tlMatch) {
    result.timelimit = tlMatch[1].trim();
  }

  const descMatch = html.match(/<div class="description">([\s\S]*?)<\/div>/);
  if (descMatch) {
    result.descText = stripHtml(descMatch[1]);
  }

  // Try Portuguese then English for Input
  let inputMatch = html.match(/<h2>Entrada<\/h2>\s*<div class="input">([\s\S]*?)<\/div>/);
  if (!inputMatch) inputMatch = html.match(/<h2>Input<\/h2>\s*<div class="input">([\s\S]*?)<\/div>/);
  if (inputMatch) {
    result.inputText = stripHtml(inputMatch[1]);
  }

  // Try Portuguese then English for Output
  let outputMatch = html.match(/<h2>Sa(?:í|&iacute;)da<\/h2>\s*<div class="output">([\s\S]*?)<\/div>/);
  if (!outputMatch) outputMatch = html.match(/<h2>Output<\/h2>\s*<div class="output">([\s\S]*?)<\/div>/);
  if (outputMatch) {
    result.outputText = stripHtml(outputMatch[1]);
  }

  // Extract examples from tables
  const tableRegex = /<table[\s\S]*?<tbody>([\s\S]*?)<\/tbody>[\s\S]*?<\/table>/g;
  let tableMatch;
  while ((tableMatch = tableRegex.exec(html)) !== null) {
    const tbody = tableMatch[1];
    const rowRegex = /<tr>([\s\S]*?)<\/tr>/g;
    let rowMatch;
    while ((rowMatch = rowRegex.exec(tbody)) !== null) {
      const cellRegex = /<td[^>]*>([\s\S]*?)<\/td>/g;
      const cells = [];
      let cellMatch;
      while ((cellMatch = cellRegex.exec(rowMatch[1])) !== null) {
        cells.push(cellMatch[1]
          .replace(/<br\s*\/?>/gi, '\n')
          .replace(/<[^>]+>/g, '')
          .replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&')
          .replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&nbsp;/g, ' ')
          .trim());
      }
      if (cells.length >= 2) {
        result.examples.push({ input: cells[0], output: cells[1] });
      }
    }
  }

  return result;
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

function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function main() {
  let processed = 0;
  let skipped = 0;
  const failed = [];

  for (let i = 0; i < problems.length; i++) {
    const p = problems[i];
    const filename = `${p.id}_${sanitizeName(p.name)}.md`;
    const filepath = path.join(dir, filename);

    // Skip if already exists
    if (fs.existsSync(filepath)) {
      skipped++;
      processed++;
      continue;
    }

    try {
      const url = `https://resources.beecrowd.com/repository/UOJ_${p.id}.html`;
      const html = await fetchURL(url);
      const data = parseHTML(html);
      const md = buildMarkdown(p.id, p.name, p.subject, p.level, data);
      fs.writeFileSync(filepath, md, 'utf8');
      processed++;

      if (processed % 25 === 0) {
        console.log(`Progress: ${processed}/${problems.length} (skipped ${skipped})`);
      }

      // Small delay to be polite to the server
      await delay(200);
    } catch (err) {
      failed.push({ id: p.id, error: err.message });
      console.error(`Failed ${p.id}: ${err.message}`);
    }
  }

  console.log(`\nDone! Processed: ${processed}, Skipped: ${skipped}, Failed: ${failed.length}`);
  if (failed.length > 0) {
    console.log('Failed IDs:', failed.map(f => f.id).join(', '));
    fs.writeFileSync(path.join(dir, '_failed.json'), JSON.stringify(failed, null, 2), 'utf8');
  }
}

main().catch(console.error);
