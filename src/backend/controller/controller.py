from modules.grammar import GrammarModule

class SapientiaLuxController:
    def __init__(self):
        self.modules = {
            "grammar": GrammarModule()
        }

    def process_request(self, module_name: str, input_data: dict) -> dict:
        """Route request to the specified module."""
        module = self.modules.get(module_name)
        if module:
            return module.correct_text(input_data.get("text", ""))
        return {"status": "error", "message": f"Module {module_name} not found"}

if __name__ == "__main__":
    controller = SapientiaLuxController()
    result = controller.process_request("grammar", {"text": "He go to school"})
    print(result)