{
"action_title": "Get Kubernetes Status for a POD in a given Namespace",
"action_description": "Get Kubernetes Status for a POD in a given Namespace",
"action_type": "LEGO_TYPE_K8S",
"action_entry_function": "k8s_get_pod_status",
"action_needs_credential": true,
"action_supports_poll": true,
"action_supports_iteration": true,
"action_output_type": "ACTION_OUTPUT_TYPE_DICT",
"action_verbs": [
"get"
],
"action_nouns": [
"status",
"kubernetes",
"pod",
"namespace"
]
}