const { BrowserWindow, app, ipcMain }  = require("electron");
const {resolve} = require("path");
const absolutePath = resolve('./preload.js')

const { spawn } = require('child_process');

function createWindow() {
    const win = new BrowserWindow({
        autoHideMenuBar: true,
        width: 1200,
        height: 800,
        icon:'./logo.jpg',
        backgroundColor: "white",
        webPreferences: {
            nodeIntegration: false,
            worldSafeExecuteJavascript: true,
            contextIsolation: true,
            preload: String(absolutePath),
        }
    })

    win.loadFile('index.html');
}



ipcMain.on('notify', (_, message) => {
    args = String(message).split("/")
    spawn('python', ['./maersk.py', String(args[0]), String(args[1])])
})
    

app.whenReady().then(createWindow)
