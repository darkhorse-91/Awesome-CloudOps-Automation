{
"action_title": " List of EKS deployment for given Namespace",
"action_description": " Get list of EKS deployment names for given Namespace",
"action_type": "LEGO_TYPE_AWS",
"action_entry_function": "aws_eks_get_deployments_name",
"action_needs_credential": true,
"action_supports_poll": true,
"action_output_type": "ACTION_OUTPUT_TYPE_LIST",
"action_supports_iteration": true,
"action_verbs": [
"list"
],
"action_nouns": [
"eks",
"deployment",
"namespace"
]
}