const lightNovelResolvers = require("./lightNovelResolvers");

module.exports = {
    Query: {
        ...lightNovelResolvers.Query,
    },

    Mutation: {
        ...lightNovelResolvers.Mutation,
    },
};
