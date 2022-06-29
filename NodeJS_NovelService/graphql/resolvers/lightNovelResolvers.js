const lightNovels = require("../../data.json").lightNovels;

const authorClient = require("../../grpcServices/authorClient");

module.exports = {
    Query: {
        listLightNovels: async () => {
            for (let novel of lightNovels) {
                await assignAuthor(novel);
            }

            return lightNovels;
        },

        getLightNovel: async (_, { id }) => {
            const lightNovel = lightNovels.find(
                (lightNovel) => lightNovel.id === id
            );

            await assignAuthor(lightNovel);

            return lightNovel;
        },
    },

    Mutation: {
        createLightNovel: async (_, { lightNovel }) => {
            lightNovel.id = lightNovels.length + 1;

            lightNovels.push(lightNovel);
            return lightNovel;
        },

        deleteLightNovel: async (_, { id }) => {
            const lightNovel = lightNovels.find(
                (lightNovel) => lightNovel.id === id
            );

            if (!lightNovel) {
                throw new Error(`Light novel with id ${id} not found`);
            }

            lightNovels.splice(lightNovels.indexOf(lightNovel), 1);

            return lightNovel;
        },

        updateLightNovel: async (_, { id, lightNovel }) => {
            const existingLightNovel = lightNovels.find(
                (lightNovel) => lightNovel.id === id
            );

            if (!existingLightNovel) {
                throw new Error(`Light novel with id ${id} not found`);
            }

            for (let key in lightNovel) {
                if (lightNovel[key]) {
                    existingLightNovel[key] = lightNovel[key];
                }
            }

            await assignAuthor(existingLightNovel);

            return existingLightNovel;
        },
    },
};

async function assignAuthor(lightNovel) {
    return new Promise((resolve, reject) =>
        authorClient.GetAuthor({ id: lightNovel.authorId }, (err, res) => {
            if (err) {
                return reject(err);
            }

            resolve(res);
        })
    ).then((author) => {
        lightNovel.author = {
            id: author.id,
            jpName: author.jp_name,
            romajiName: author.romaji_name,
            twitter: author.twitter,
        };
    });
}
