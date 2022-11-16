{
"action_title": "Get AWS EC2 CPU Utilization Statistics from Cloudwatch",
"action_description": "Get AWS CloudWatch Statistics for cpu utilization for EC2 instances",
"action_type": "LEGO_TYPE_AWS",
"action_entry_function": "aws_get_cloudwatch_ec2_cpuutil",
"action_needs_credential": true,
"action_supports_poll": true,
"action_output_type": "ACTION_OUTPUT_TYPE_STR",
"action_supports_iteration": true,
"action_verbs": [
"get"
],
"action_nouns": [
"aws",
"cloudwatch",
"statistics",
"cpu",
"utilization"
]
}