def do_intervention(schedule, intervention, **kwargs):
    intervention_name = intervention.__name__ + 'Instance'
    if hasattr(schedule, intervention_name):
        interventionInstance = getattr(schedule, intervention_name)
        interventionInstance.intervention(schedule, **kwargs)
