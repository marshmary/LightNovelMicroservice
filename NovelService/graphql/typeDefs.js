const { gql } = require("apollo-server");

module.exports = gql`
    type Author {
        id: Int
        jpName: String
        romajiName: String
        twitter: String
    }

    type LightNovel {
        id: Int
        jpName: String
        romajiName: String
        volumes: Int
        extras: Int
        authorId: Int
        author: Author
    }

    input LightNovelInput {
        jpName: String
        romajiName: String
        volumes: Int
        extras: Int
        authorId: Int
    }

    type Query {
        listLightNovels: [LightNovel]
        getLightNovel(id: Int!): LightNovel
    }

    type Mutation {
        createLightNovel(lightNovel: LightNovelInput): LightNovel
        deleteLightNovel(id: Int!): LightNovel
        updateLightNovel(id: Int!, lightNovel: LightNovelInput): LightNovel
    }
`;
