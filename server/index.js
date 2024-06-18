const express = require("express");
const app = express();
const http = require("http");
const {Server} = require("socket.io");
const cors = require("cors");
const axios = require("axios")

const {spawn} = require("child_process")



app.use(cors());

const server = http.createServer(app)

const io = new Server(server, {
    cors: {
        origin: "http://localhost:3000",
        methods: ["GET", "POST"],
    },
});


io.on("connection", (socket) => {
    console.log(`User Connected: ${socket.id}`)

    socket.on("send_message", (data) => {
        const pythonProcess = spawn('python', ['../llm/llm_calling.py'])
        pythonProcess.stdin.write(data.message + '\n')
        pythonProcess.stdin.end();

        pythonProcess.stdout.on('data', (output) => {
            const llm_response = output.toString().trim();
            socket.emit("recieve_message", {message: llm_response})
        });
        
    } )
})

server.listen(3001, () => {
    console.log("SERVER IS RUNNING")
})

