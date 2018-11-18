import json

class abet_model_util:

    def is_json(self, json_in):
        try:
            json_object = json.loads(json_in)
        except ValueError as e:
            return False
        return True

    def transform_from_post_response(self, request, app):
        for key, value in request.POST.items():
            # print("key: %s <==> value: %s" % (key, value))
            if "programName" in key:
                app.program_name = value
            elif "streetAddress" in key:
                app.street_address = value
            elif "city" in key:
                app.city = value
            elif "zipCode" in key:
                app.zip = value
            elif "contactPerson" in key:
                app.contact_person = value
            elif "contactPhone" in key:
                app.contact_phone = value
            elif "contactEmail" in key:
                app.contact_email = value
            elif "Program" in key:
                app.program = value
            elif "jobTitle" in key:
                app.job_title = value
            else:
                pass

