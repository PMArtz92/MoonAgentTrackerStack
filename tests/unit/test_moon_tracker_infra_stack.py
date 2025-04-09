import aws_cdk as core
import aws_cdk.assertions as assertions

from moon_tracker_infra.moon_tracker_infra_stack import MoonTrackerInfraStack

# example tests. To run these tests, uncomment this file along with the example
# resource in moon_tracker_infra/moon_tracker_infra_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MoonTrackerInfraStack(app, "moon-tracker-infra")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
