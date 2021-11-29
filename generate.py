from transformers import pipeline

# generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

# generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')

while True:

    prompt = input("YOU: ")

    res = generator(prompt, max_length=30, do_sample=True, temperature=0.5)

    result = res[0]['generated_text'].split(".")

    print(str("BOT: " + result[0] + ".").replace(prompt, " "))
