import fs from 'fs';

export function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) return reject(err);

      const lines = data.trim().split('\n');
      const fields = {};

      // Başlık satırını atla
      const header = lines.shift();

      lines.forEach(line => {
        const [firstname, , field] = line.split(',');
        if (!fields[field]) fields[field] = [];
        fields[field].push(firstname);
      });

      resolve(fields);
    });
  });
}
