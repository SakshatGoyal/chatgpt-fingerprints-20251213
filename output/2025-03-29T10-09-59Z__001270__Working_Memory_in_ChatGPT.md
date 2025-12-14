# Working Memory in ChatGPT

## You (2025-03-29T10:09:59.089981+00:00)

Hey, I want to get a better understanding of how working memory works with ChatGPT.

## ChatGPT (2025-03-29T10:09:59.114929+00:00)

Sure, let's break it down! Working memory for ChatGPT is kind of like a conversation buffer. During a chat, I can keep track of the context from earlier messages, which helps me provide relevant responses. Once a session ends, though, I don't retain that info. So, it's like having a short-term memory that resets between conversations. Does that help?

## You (2025-03-29T10:10:56.714886+00:00)

Yeah, I think I get the idea, but I want to understand it from a more token-centered perspective. So, help me understand, let's say I have a conversation with ChatGPT, and every time I send a message, I send it roughly 300 tokens. So, how many of those tokens are stored as working memory? So, how many of those tokens are stored as working memory?

## ChatGPT (2025-03-29T10:10:56.741417+00:00)

Got it! So, ChatGPT's working memory depends on the context window, which is the maximum number of tokens it can keep in mind at once. This includes both the user's inputs and the model's responses. For instance, if the context window is 4,000 tokens, the model can remember the last 4,000 tokens of the conversation. When you reach that limit, older tokens start to get forgotten as new ones come in. So, it acts like a sliding window.

## You (2025-03-29T10:11:21.807189+00:00)

So what's the max token limit for any conversation with ChatGPT, the 4.0 model?

## ChatGPT (2025-03-29T10:11:21.871632+00:00)

For the GPT-4o model, the context window is typically around 128,000 tokens! This means it can remember a pretty extensive chunk of your conversation before older messages start getting trimmed out.

## You (2025-03-29T10:12:02.749059+00:00)

Help me understand how much 128,000 tokens is, like in terms of books or pages or whatever kind of rubric metric you want to use.

## ChatGPT (2025-03-29T10:12:02.790729+00:00)

Sure! 128,000 tokens is quite a lot. If we convert that to words, it's roughly 90,000 to 100,000 words. For perspective, a typical novel is around 80,000 to 100,000 words. So, that's about the length of a full novel!

## You (2025-03-29T10:13:26.741323+00:00)

Okay, now, remembering words is one thing, remembering meaning is something else. So, for example, I could be having a conversation, a very detailed, in-depth sort of analytical conversation with ChatGPT. I'm sure some amount of effort would have to go into actually deriving meaning through a conversation and also storing the sort of meaning within all the sort of chat window. Does meaning, I know it's an ambiguous word, but does meaning itself hold or weigh some kind of tokens?

## ChatGPT (2025-03-29T10:13:26.779955+00:00)

Great question! Yes, deriving and storing "meaning" is a bit more nuanced than just counting words. Each token represents a small chunk of text, and the model processes these chunks to understand context, relationships, and implications. While "meaning" itself doesn't have a direct token count, the model's capacity to remember and integrate meaning depends on how those tokens are used. So, complex, detailed conversations mean more tokens are used to capture nuances, leaving less space for new information.

## You (2025-03-29T10:13:57.432176+00:00)

Does it work the same way with Gemini?

## ChatGPT (2025-03-29T10:13:57.474237+00:00)

Gemini models have similar principles regarding context windows and token limits. They process tokens to understand and generate responses, just like GPT models. The specifics, like the maximum token count, might differ depending on the Gemini model version. But the general idea of managing context, meaning, and token usage remains the same.

## You (2025-03-29T10:14:25.833319+00:00)

Okay, I'm using Gemini 2.5 Pro.

## ChatGPT (2025-03-29T10:14:25.884127+00:00)

Got it! Gemini 2.5 Pro is quite advanced and likely has a substantial context window, similar to other state-of-the-art models. While exact token limits can vary, it should handle detailed and lengthy conversations effectively, balancing context and meaning well. If you're having deep, analytical discussions, it should retain a lot of relevant information for coherent responses!
