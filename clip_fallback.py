class CLIPFallback:

    FUNCTION = "run"
    CATEGORY = "Krystal/Fallbacks"
    RETURN_TYPES = ("CLIP",)
    RETURN_NAMES = ("clip",)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "clip_primary": ("CLIP",),
                "clip_fallback": ("CLIP",),
            }
        }

    def run(self, clip_primary=None, clip_fallback=None):
        if clip_primary is not None:
            return (clip_primary,)
        return (clip_fallback,)


NODE_CLASS_MAPPINGS = {
    "CLIPFallback": CLIPFallback
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CLIPFallback": "CLIP Fallback"
}