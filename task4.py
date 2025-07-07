# Google Colab

from diffusers import StableDiffusionPipeline
import torch
import matplotlib.pyplot as plt

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda" if torch.cuda.is_available() else "cpu"

if device == "cuda":
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float16
    ).to(device)
else:
    pipe = StableDiffusionPipeline.from_pretrained(model_id).to(device)

print("Model loaded successfully!")

prompt = input("Enter your prompt for image generation: ")

print("Generating image...")
result = pipe(prompt)
image = result.images[0]
print("Image generation complete.")

plt.imshow(image)
plt.axis('off')
plt.show()

image.save("generated_image.png")
print("Image saved as generated_image.png")
