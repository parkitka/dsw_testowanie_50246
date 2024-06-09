from allure_commons.types import AttachmentType
import allure


def before_all(context):
    pass  # Placeholder for future code


def after_all(context):
    allure.dynamic.environment(browser="Chrome")
    allure.dynamic.environment(url="https://reqres.in/api/")


def after_step(context, step):
    if step.status == "failed":
        try:
            allure.attach(context.driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
        except AttributeError as e:
            print("Screenshot not taken:", e)
