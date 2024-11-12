import torch
from diffusers import StableDiffusionPipeline

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"


pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to(device)

prompt = "upgraded transhuman form. Cyberpunk. Dark and Gritty. Surreal. Kodak Kodachrome"
image = pipe(prompt).images[0]  
    
image.save("upgraded_transhuman_form.png")