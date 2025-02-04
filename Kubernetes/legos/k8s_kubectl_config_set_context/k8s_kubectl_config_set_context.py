from pydantic import BaseModel, Field


class InputSchema(BaseModel):
    k8s_cli_string: str = Field(
        title='Kubectl Command',
        description='kubectl sets a context entry in kubeconfig',
        default='kubectl config set-context --current --namespace={namespace}'
    )
    namespace: str = Field(
        title='Namespace',
        description='Namespace'
    )

def k8s_kubectl_config_set_context_printer(data: list):
    if data is None:
        return

    print (data)

def k8s_kubectl_config_set_context(handle, k8s_cli_string: str, namespace: str) -> list:
    """k8s_kubectl_config_set_context 

        :type handle: object
        :param handle: Object returned from the Task validate method

        :type k8s_cli_string: str
        :param k8s_cli_string: kubectl sets a context entry in kubeconfig

        :type namespace: str
        :param namespace: Namespace

        :rtype: List
    """
    k8s_cli_string = k8s_cli_string.format(namespace=namespace)
    result = handle.run_native_cmd(k8s_cli_string)
    if result is None or hasattr(result, "stderr") is False or result.stderr is None:
        return None

    return result.stdout
