from polarizer.clients import TrackerClient


def get_requirement(config, productId='RHSAT6', requirementId='RHSAT6-39825'):
    client = TrackerClient(config)
    return client.service.getWorkItemById(productId, requirementId)
