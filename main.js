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
    if (args[0] == "m") {
        spawn('python', ['./maersk.py', String(args[1]), String(args[2])])
    } else if (args[0] == "c") {
        spawn('python', ['./cmagcm.py', String(args[1]), String(args[2])])
    } else if (args[0] == "h") {
        spawn('python', ['./happag.py', String(args[1]), String(args[2])])
    } else {
        console.log("Invalid Keyword")
    }
})
    

app.whenReady().then(createWindow)
