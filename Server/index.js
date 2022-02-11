import express from 'express'
import Database from './database.js';
import cors from 'cors';
import helmet from 'helmet'
import rateLimit from 'express-rate-limit';

const PORT = 8000

const limiter = rateLimit({
    windowMs: 15 * 60 * 1000, 
    max: 100 
});

const corsOption = {
    optionsSuccessStatus: 200,
    methods: "POST"
}

const standardizeInput = (req, res, next) => {
    req.body.line = encodeURI(req.body.line)
    next()
}

class Server {
    constructor (port) {
        this.port = port;
        this.app = express()
        this.init()
        this.listen(port)
        //this.database = new Database(...)
    }
    
    router = () => {
        this.app.post('/analyse', async (req, res) => {
            // res = predict(req.body.line, req.body.emotion)
            let prediction = true
            res.send(prediction)
        })
    }

    init = () => {
        this.app.use(cors(corsOption))
        this.app.use(express.json());
        this.app.use(express.urlencoded({extended: true}));
        this.app.use(helmet())
        this.app.use(limiter);
        this.app.use(standardizeInput)
        this.router()
    }

    listen = (port) => {
        this.app.listen(port, () => {
            console.log(`App listening at http://localhost:${port}`)
        })
    }
    
}

new Server(PORT)