const path = require("path");
const grpc = require("grpc");
const fs = require("fs");

const PROTO_PATH = path.resolve(__dirname, "../protos/author.proto");
const AUTHOR_SERVICE_URL = "localhost:50051";

const AuthorService = grpc.load(PROTO_PATH).GrpcAuthors;

// const cert = fs.readFileSync("localhost.pem");

// console.log(cert);

const client = new AuthorService(
    AUTHOR_SERVICE_URL,
    // grpc.credentials.createSsl(cert)
    grpc.credentials.createInsecure()
);

module.exports = client;
