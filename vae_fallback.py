class VAEFallback:

    FUNCTION = "run"
    CATEGORY = "Krystal/Fallbacks"
    RETURN_TYPES = ("VAE",)
    RETURN_NAMES = ("vae",)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "vae_primary": ("VAE",),
                "vae_fallback": ("VAE",),
            }
        }

    def run(self, vae_primary=None, vae_fallback=None):
        if vae_primary is not None:
            return (vae_primary,)
        return (vae_fallback,)


NODE_CLASS_MAPPINGS = {
    "VAEFallback": VAEFallback
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "VAEFallback": "VAE Fallback"
}