const fs = require('fs');
const path = require('path');

const problems = JSON.parse(fs.readFileSync('/home/brunodcdo/Desktop/dev/2026/23_URI/problems_list.json', 'utf8'));
const dir = '/home/brunodcdo/Desktop/dev/2026/23_URI/beecrowd_iniciante';
const dataDir = '/home/brunodcdo/Desktop/dev/2026/23_URI/batch_data';

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

// Read all batch JSON files and create markdown files
const batchFiles = fs.readdirSync(dataDir).filter(f => f.startsWith('batch_') && f.endsWith('.json')).sort();
let totalSaved = 0;
let totalFailed = 0;

const problemMap = {};
for (const p of problems) {
  problemMap[p.id] = p;
}

for (const batchFile of batchFiles) {
  const data = JSON.parse(fs.readFileSync(path.join(dataDir, batchFile), 'utf8'));

  for (const [id, content] of Object.entries(data)) {
    if (content.error) {
      totalFailed++;
      continue;
    }

    const p = problemMap[id];
    if (!p) continue;

    const filename = `${p.id}_${sanitizeName(p.name)}.md`;
    const filepath = path.join(dir, filename);
    const md = buildMarkdown(p.id, p.name, p.subject, p.level, content);
    fs.writeFileSync(filepath, md, 'utf8');
    totalSaved++;
  }
}

console.log(`Saved: ${totalSaved}, Failed: ${totalFailed}`);
console.log(`Batch files processed: ${batchFiles.length}`);
