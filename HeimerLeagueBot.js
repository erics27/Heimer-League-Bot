const Discord = require("discord.js")
const fetch = require("node-fetch")
const client = new Discord.Client({
    intents:[Discord.Intents.FLAGS.GUILDS,
        Discord.Intents.FLAGS.GUILD_MEMBERS,
        Discord.Intents.FLAGS.GUILD_BANS,
        Discord.Intents.FLAGS.GUILD_EMOJIS_AND_STICKERS,
        Discord.Intents.FLAGS.GUILD_INTEGRATIONS,
        Discord.Intents.FLAGS.GUILD_WEBHOOKS,
        Discord.Intents.FLAGS.GUILD_INVITES,
        Discord.Intents.FLAGS.GUILD_VOICE_STATES,
        Discord.Intents.FLAGS.GUILD_PRESENCES,
        Discord.Intents.FLAGS.GUILD_MESSAGES,
        Discord.Intents.FLAGS.GUILD_MESSAGE_REACTIONS,
        Discord.Intents.FLAGS.GUILD_MESSAGE_TYPING,
        Discord.Intents.FLAGS.DIRECT_MESSAGES,
        Discord.Intents.FLAGS.DIRECT_MESSAGE_REACTION,
        Discord.Intents.FLAGS.DIRECT_MESSAGE_TYPING]
    // intents:[Discord.Intents.FLAGS.GUILD_EMOJIS_AND_STICKERS]
    // intents: [Discord.Intents.FLAGS.GUILD_MESSAGES, Discord.Intents.FLAGS.GUILD_MESSAGE_TYPING, Discord.Intents.FLAGS.DIRECT_MESSAGE_TYPING, Discord.Intents.FLAGS.DIRECT_MESSAGES]
})

function getQuote() {
	return fetch("https://zenquotes.io/api/random")
		.then(res => {
			return res.json()
		})
		.then(data => {
			return data[0]["q"] + " -" + data[0]["a"]
		})
}

client.on("ready", () => {
    console.log('logged in as ${client.user.tag}!')
})

client.on("message", msg => {
	if (msg.author.bot) return

	if (msg.content == "$inspire") {
		getQuote().then(quote => msg.channel.send(quote))
	}
    if (msg.content === "test") {
        msg.reply("pickle rick")
    }
})

client.login('OTExNTAxMzU5Nzk3Mzg3Mjg1.YZiTyw.1KBGyMSyac310ahf9tpy_R0NG9E')
