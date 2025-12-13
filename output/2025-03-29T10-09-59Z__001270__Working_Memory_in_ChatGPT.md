# Working Memory in ChatGPT

## You (2025-03-29T10:09:59.089981+00:00)

{'content_type': 'audio_transcription', 'text': 'Hey, I want to get a better understanding of how working memory works with ChatGPT.', 'direction': 'in', 'decoding_id': None}
{'expiry_datetime': '2025-04-28T10:09:58.901849+00:00', 'content_type': 'real_time_user_audio_video_asset_pointer', 'frames_asset_pointers': [], 'video_container_asset_pointer': None, 'audio_asset_pointer': {'expiry_datetime': '2025-04-28T10:09:58.901849+00:00', 'content_type': 'audio_asset_pointer', 'asset_pointer': 'sediment://file_000000005ed851f6b1bf85601f65744a', 'size_bytes': 272238, 'format': 'wav', 'metadata': {'start_timestamp': None, 'end_timestamp': None, 'pretokenized_vq': None, 'interruptions': None, 'original_audio_source': None, 'transcription': None, 'word_transcription': None, 'start': Decimal('0.0'), 'end': Decimal('5.67')}}, 'audio_start_timestamp': Decimal('14.029907913180068')}

## ChatGPT (2025-03-29T10:09:59.114929+00:00)

{'content_type': 'audio_transcription', 'text': "Sure, let's break it down! Working memory for ChatGPT is kind of like a conversation buffer. During a chat, I can keep track of the context from earlier messages, which helps me provide relevant responses. Once a session ends, though, I don't retain that info. So, it's like having a short-term memory that resets between conversations. Does that help?", 'direction': 'out', 'decoding_id': None}
{'expiry_datetime': '2025-04-28T10:09:58.901935+00:00', 'content_type': 'audio_asset_pointer', 'asset_pointer': 'sediment://file_000000006dec51f6bfee54c80ca0c0e8', 'size_bytes': 844878, 'format': 'wav', 'metadata': {'start_timestamp': None, 'end_timestamp': None, 'pretokenized_vq': None, 'interruptions': None, 'original_audio_source': None, 'transcription': None, 'word_transcription': None, 'start': Decimal('0.0'), 'end': Decimal('17.6')}}

## You (2025-03-29T10:10:56.714886+00:00)

{'content_type': 'audio_transcription', 'text': "Yeah, I think I get the idea, but I want to understand it from a more token-centered perspective. So, help me understand, let's say I have a conversation with ChatGPT, and every time I send a message, I send it roughly 300 tokens. So, how many of those tokens are stored as working memory? So, how many of those tokens are stored as working memory?", 'direction': 'in', 'decoding_id': None}
{'expiry_datetime': '2025-04-28T10:10:56.566083+00:00', 'content_type': 'real_time_user_audio_video_asset_pointer', 'frames_asset_pointers': [], 'video_container_asset_pointer': None, 'audio_asset_pointer': {'expiry_datetime': '2025-04-28T10:10:56.566083+00:00', 'content_type': 'audio_asset_pointer', 'asset_pointer': 'sediment://file_00000000ebac51f696b4bf52b4929089', 'size_bytes': 1450158, 'format': 'wav', 'metadata': {'start_timestamp': None, 'end_timestamp': None, 'pretokenized_vq': None, 'interruptions': None, 'original_audio_source': None, 'transcription': None, 'word_transcription': None, 'start': Decimal('0.0'), 'end': Decimal('30.21')}}, 'audio_start_timestamp': Decimal('64.97896974603646')}

## ChatGPT (2025-03-29T10:10:56.741417+00:00)

{'content_type': 'audio_transcription', 'text': "Got it! So, ChatGPT's working memory depends on the context window, which is the maximum number of tokens it can keep in mind at once. This includes both the user's inputs and the model's responses. For instance, if the context window is 4,000 tokens, the model can remember the last 4,000 tokens of the conversation. When you reach that limit, older tokens start to get forgotten as new ones come in. So, it acts like a sliding window.", 'direction': 'out', 'decoding_id': None}
{'expiry_datetime': '2025-04-28T10:10:56.566184+00:00', 'content_type': 'audio_asset_pointer', 'asset_pointer': 'sediment://file_00000000fef451f6aa658a6f23a67fb7', 'size_bytes': 1166478, 'format': 'wav', 'metadata': {'start_timestamp': None, 'end_timestamp': None, 'pretokenized_vq': None, 'interruptions': None, 'original_audio_source': None, 'transcription': None, 'word_transcription': None, 'start': Decimal('0.0'), 'end': Decimal('24.3')}}

## You (2025-03-29T10:11:21.807189+00:00)

{'content_type': 'audio_transcription', 'text': "So what's the max token limit for any conversation with ChatGPT, the 4.0 model?", 'direction': 'in', 'decoding_id': None}
{'expiry_datetime': '2025-04-28T10:11:21.615919+00:00', 'content_type': 'real_time_user_audio_video_asset_pointer', 'frames_asset_pointers': [], 'video_container_asset_pointer': None, 'audio_asset_pointer': {'expiry_datetime': '2025-04-28T10:11:21.615919+00:00', 'content_type': 'audio_asset_pointer', 'asset_pointer': 'sediment://file_00000000887051f6aeb361a0647ddbd4', 'size_bytes': 361038, 'format': 'wav', 'metadata': {'start_timestamp': None, 'end_timestamp': None, 'pretokenized_vq': None, 'interruptions': None, 'original_audio_source': None, 'transcription': None, 'word_transcription': None, 'start': Decimal('0.0'), 'end': Decimal('7.52')}}, 'audio_start_timestamp': Decimal('103.69439574913122')}

## ChatGPT (2025-03-29T10:11:21.871632+00:00)

{'content_type': 'audio_transcription', 'text': 'For the GPT-4o model, the context window is typically around 128,000 tokens! This means it can remember a pretty extensive chunk of your conversation before older messages start getting trimmed out.', 'direction': 'out', 'decoding_id': None}
{'expiry_datetime': '2025-04-28T10:11:21.616041+00:00', 'content_type': 'audio_asset_pointer', 'asset_pointer': 'sediment://file_00000000b2ec51f6be134fb7b581685b', 'size_bytes': 506478, 'format': 'wav', 'metadata': {'start_timestamp': None, 'end_timestamp': None, 'pretokenized_vq': None, 'interruptions': None, 'original_audio_source': None, 'transcription': None, 'word_transcription': None, 'start': Decimal('0.0'), 'end': Decimal('10.55')}}

## You (2025-03-29T10:12:02.749059+00:00)

{'content_type': 'audio_transcription', 'text': 'Help me understand how much 128,000 tokens is, like in terms of books or pages or whatever kind of rubric metric you want to use.', 'direction': 'in', 'decoding_id': None}
{'expiry_datetime': '2025-04-28T10:12:02.537453+00:00', 'content_type': 'real_time_user_audio_video_asset_pointer', 'frames_asset_pointers': [], 'video_container_asset_pointer': None, 'audio_asset_pointer': {'expiry_datetime': '2025-04-28T10:12:02.537453+00:00', 'content_type': 'audio_asset_pointer', 'asset_pointer': 'sediment://file_00000000959851f6beb2a0875e12fb46', 'size_bytes': 534798, 'format': 'wav', 'metadata': {'start_timestamp': None, 'end_timestamp': None, 'pretokenized_vq': None, 'interruptions': None, 'original_audio_source': None, 'transcription': None, 'word_transcription': None, 'start': Decimal('0.0'), 'end': Decimal('11.14')}}, 'audio_start_timestamp': Decimal('140.01992147415876')}

## ChatGPT (2025-03-29T10:12:02.790729+00:00)

{'content_type': 'audio_transcription', 'text': "Sure! 128,000 tokens is quite a lot. If we convert that to words, it's roughly 90,000 to 100,000 words. For perspective, a typical novel is around 80,000 to 100,000 words. So, that's about the length of a full novel!", 'direction': 'out', 'decoding_id': None}
{'expiry_datetime': '2025-04-28T10:12:02.537543+00:00', 'content_type': 'audio_asset_pointer', 'asset_pointer': 'sediment://file_00000000419451f6a872018465c9cc00', 'size_bytes': 734478, 'format': 'wav', 'metadata': {'start_timestamp': None, 'end_timestamp': None, 'pretokenized_vq': None, 'interruptions': None, 'original_audio_source': None, 'transcription': None, 'word_transcription': None, 'start': Decimal('0.0'), 'end': Decimal('15.3')}}

## You (2025-03-29T10:13:26.741323+00:00)

{'content_type': 'audio_transcription', 'text': "Okay, now, remembering words is one thing, remembering meaning is something else. So, for example, I could be having a conversation, a very detailed, in-depth sort of analytical conversation with ChatGPT. I'm sure some amount of effort would have to go into actually deriving meaning through a conversation and also storing the sort of meaning within all the sort of chat window. Does meaning, I know it's an ambiguous word, but does meaning itself hold or weigh some kind of tokens?", 'direction': 'in', 'decoding_id': None}
{'expiry_datetime': '2025-04-28T10:13:26.548573+00:00', 'content_type': 'real_time_user_audio_video_asset_pointer', 'frames_asset_pointers': [], 'video_container_asset_pointer': None, 'audio_asset_pointer': {'expiry_datetime': '2025-04-28T10:13:26.548573+00:00', 'content_type': 'audio_asset_pointer', 'asset_pointer': 'sediment://file_00000000c57851f694d43d6f4ee8ffab', 'size_bytes': 2187918, 'format': 'wav', 'metadata': {'start_timestamp': None, 'end_timestamp': None, 'pretokenized_vq': None, 'interruptions': None, 'original_audio_source': None, 'transcription': None, 'word_transcription': None, 'start': Decimal('0.0'), 'end': Decimal('45.58')}}, 'audio_start_timestamp': Decimal('213.24772484204732')}

## ChatGPT (2025-03-29T10:13:26.779955+00:00)

{'content_type': 'audio_transcription', 'text': 'Great question! Yes, deriving and storing "meaning" is a bit more nuanced than just counting words. Each token represents a small chunk of text, and the model processes these chunks to understand context, relationships, and implications. While "meaning" itself doesn\'t have a direct token count, the model\'s capacity to remember and integrate meaning depends on how those tokens are used. So, complex, detailed conversations mean more tokens are used to capture nuances, leaving less space for new information.', 'direction': 'out', 'decoding_id': None}
{'expiry_datetime': '2025-04-28T10:13:26.548677+00:00', 'content_type': 'audio_asset_pointer', 'asset_pointer': 'sediment://file_000000006b9851f69df0b3e114d74f22', 'size_bytes': 1238478, 'format': 'wav', 'metadata': {'start_timestamp': None, 'end_timestamp': None, 'pretokenized_vq': None, 'interruptions': None, 'original_audio_source': None, 'transcription': None, 'word_transcription': None, 'start': Decimal('0.0'), 'end': Decimal('25.8')}}

## You (2025-03-29T10:13:57.432176+00:00)

{'content_type': 'audio_transcription', 'text': 'Does it work the same way with Gemini?', 'direction': 'in', 'decoding_id': None}
{'expiry_datetime': '2025-04-28T10:13:57.323425+00:00', 'content_type': 'real_time_user_audio_video_asset_pointer', 'frames_asset_pointers': [], 'video_container_asset_pointer': None, 'audio_asset_pointer': {'expiry_datetime': '2025-04-28T10:13:57.323425+00:00', 'content_type': 'audio_asset_pointer', 'asset_pointer': 'sediment://file_00000000a76851f6b482e179fd9fd6c2', 'size_bytes': 103278, 'format': 'wav', 'metadata': {'start_timestamp': None, 'end_timestamp': None, 'pretokenized_vq': None, 'interruptions': None, 'original_audio_source': None, 'transcription': None, 'word_transcription': None, 'start': Decimal('0.0'), 'end': Decimal('2.15')}}, 'audio_start_timestamp': Decimal('250.85016755503602')}

## ChatGPT (2025-03-29T10:13:57.474237+00:00)

{'content_type': 'audio_transcription', 'text': 'Gemini models have similar principles regarding context windows and token limits. They process tokens to understand and generate responses, just like GPT models. The specifics, like the maximum token count, might differ depending on the Gemini model version. But the general idea of managing context, meaning, and token usage remains the same.', 'direction': 'out', 'decoding_id': None}
{'expiry_datetime': '2025-04-28T10:13:57.323519+00:00', 'content_type': 'audio_asset_pointer', 'asset_pointer': 'sediment://file_00000000e46451f688c124d140f3dd38', 'size_bytes': 892878, 'format': 'wav', 'metadata': {'start_timestamp': None, 'end_timestamp': None, 'pretokenized_vq': None, 'interruptions': None, 'original_audio_source': None, 'transcription': None, 'word_transcription': None, 'start': Decimal('0.0'), 'end': Decimal('18.6')}}

## You (2025-03-29T10:14:25.833319+00:00)

{'content_type': 'audio_transcription', 'text': "Okay, I'm using Gemini 2.5 Pro.", 'direction': 'in', 'decoding_id': None}
{'expiry_datetime': '2025-04-28T10:14:25.667941+00:00', 'content_type': 'real_time_user_audio_video_asset_pointer', 'frames_asset_pointers': [], 'video_container_asset_pointer': None, 'audio_asset_pointer': {'expiry_datetime': '2025-04-28T10:14:25.667941+00:00', 'content_type': 'audio_asset_pointer', 'asset_pointer': 'sediment://file_00000000fba451f6aac3dc3796640b73', 'size_bytes': 152718, 'format': 'wav', 'metadata': {'start_timestamp': None, 'end_timestamp': None, 'pretokenized_vq': None, 'interruptions': None, 'original_audio_source': None, 'transcription': None, 'word_transcription': None, 'start': Decimal('0.0'), 'end': Decimal('3.18')}}, 'audio_start_timestamp': Decimal('275.56485730898567')}

## ChatGPT (2025-03-29T10:14:25.884127+00:00)

{'content_type': 'audio_transcription', 'text': "Got it! Gemini 2.5 Pro is quite advanced and likely has a substantial context window, similar to other state-of-the-art models. While exact token limits can vary, it should handle detailed and lengthy conversations effectively, balancing context and meaning well. If you're having deep, analytical discussions, it should retain a lot of relevant information for coherent responses!", 'direction': 'out', 'decoding_id': None}
{'expiry_datetime': '2025-04-28T10:14:25.668037+00:00', 'content_type': 'audio_asset_pointer', 'asset_pointer': 'sediment://file_0000000080a051f69e1151f5c1a84708', 'size_bytes': 969678, 'format': 'wav', 'metadata': {'start_timestamp': None, 'end_timestamp': None, 'pretokenized_vq': None, 'interruptions': None, 'original_audio_source': None, 'transcription': None, 'word_transcription': None, 'start': Decimal('0.0'), 'end': Decimal('20.2')}}

