const child_process = require('child_process')
const webpage = process.argv[2]
let cmd

if (process.platform === 'darwin') {
  cmd = `open ${webpage}`
} else {
  cmd = `start ${webpage}`
}

child_process.execSync(cmd)
