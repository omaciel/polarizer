from polarizer.clients import PlanClient


def create_plan(
    config,
    project_id,
    plan_name,
    plan_id=None,
    parent_id=None,
    template_id='release',
):
    '''Create a new Polarion Plan.'''
    client = PlanClient(config)
    return client.service.createPlan(
        project_id,
        plan_name,
        plan_id,
        parent_id,
        template_id,
        )


def delete_plan(config, productId='RHSAT6', planId='Satellite_6_4_0'):
    '''Delete an existing Polarion plan by its ID.'''
    client = PlanClient(config)
    return client.service.deletePlans(productId, [planId])


def get_plan(config, productId='RHSAT6', planId='Satellite_6_4_0'):
    '''Fetch an existing Polarion Plan by its ID.'''
    client = PlanClient(config)
    return client.service.getPlanById(productId, planId)
