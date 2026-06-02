import folder_paths
import numpy as np
from PIL import Image
import os
import uuid

class MultiImagePreview:
    
    FUNCTION = "run"
    CATEGORY = "Krystal/Previews"
    RETURN_TYPES = ()
    OUTPUT_NODE = True
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_1": ("IMAGE",),
            }
        }
    
    def run(self, **kwargs):
        images = [v for k, v in sorted(kwargs.items()) if v is not None]
        results = []
        
        for image in images:
            i = 255. * image.cpu().numpy()[0]
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            
            filename = f"multipreview_{uuid.uuid4().hex[:8]}.png"
            temp_dir = folder_paths.get_temp_directory()
            filepath = os.path.join(temp_dir, filename)
            img.save(filepath)
            
            results.append({
                "filename": filename,
                "subfolder": "",
                "type": "temp"
            })
        
        return {"ui": {"images": results}}
    
    
NODE_CLASS_MAPPINGS = {
    "MultiImagePreview": MultiImagePreview
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MultiImagePreview": "Multi Image Preview"
}