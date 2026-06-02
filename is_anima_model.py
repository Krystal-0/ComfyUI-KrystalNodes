class IsAnimaModel:

    FUNCTION = "run"
    CATEGORY = "Krystal/Anima"
    RETURN_TYPES = ("BOOLEAN", "INT")
    RETURN_NAMES = ("boolean", "int")

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("MODEL",),
            }
        }

    def run(self, model):
        if model.model.__class__.__name__ == "Anima":
            return (True, 2)
        return (False, 1)


NODE_CLASS_MAPPINGS = {
    "IsAnimaModel": IsAnimaModel
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "IsAnimaModel": "IsAnimaModel?"
}