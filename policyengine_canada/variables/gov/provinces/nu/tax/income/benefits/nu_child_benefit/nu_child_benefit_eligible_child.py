from policyengine_canada.model_api import *


class nu_child_benefit_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Nunvaut child benefit eligible child"
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(person, period, parameters):
        age = person("age", period)
        return (
            age
            < parameters(period).gov.provinces.nu.tax.benefits.nucb.age_limit
        )
