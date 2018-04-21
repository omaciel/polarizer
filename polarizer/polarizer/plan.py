from polarizer.clients import PlanClient


def get_plan(config, productId='RHSAT6', planId='Satellite_6_4_0'):
    client = PlanClient(config)
    return client.service.getPlanById(productId, planId)