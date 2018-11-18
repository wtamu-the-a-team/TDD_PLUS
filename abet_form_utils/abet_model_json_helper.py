class abet_model_json_helper:

    def update_model_from_json_element(self, model, json_key, json_value):
        if json_key == "id":
            model.id = json_value
        elif json_key == "job_title":
            model.job_title = json_value
        else:
            pass
