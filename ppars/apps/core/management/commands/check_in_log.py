from django.core.management.base import BaseCommand
from ppars.apps.core.models import AutoRefill, Customer


class Command(BaseCommand):
    '''
    check_in_log
    '''

    def handle(self, *args, **options):
        company_id = raw_input("Enter the company id: ")
        autorefills = [6729783719234506, 6729783719234528, 6729783719234529,
                       6729783719234538,
                       6729783719234537, 6729783719234542, 6729783719237909,
                       6729783719234559,
                       6729783719237910, 6729783719234585, 6729783719234595,
                       6729783719234611,
                       6729783719234638, 6729783719234663, 6729783719234699,
                       6729783719234700,
                       6729783719234766, 6729783719234768, 6729783719234775,
                       6729783719234776,
                       6729783719234785, 6729783719234792, 6729783719234793,
                       6729783719234809,
                       6729783719234814, 6729783719234815, 6729783719234816,
                       6729783719234817,
                       6729783719234818, 6729783719234819, 6729783719234854,
                       6729783719234856,
                       6729783719234857, 6729783719234858, 6729783719234859,
                       6729783719234890,
                       6729783719234891, 6729783719234892, 6729783719234893,
                       6729783719234900,
                       6729783719234901, 6729783719234969, 6729783719234968,
                       6729783719234985,
                       6729783719234989, 6729783719234995, 6729783719234994,
                       6729783719234989,
                       6729783719234995, 6729783719235003, 6729783719235011,
                       6729783719235125,
                       6729783719235124, 6729783719235131, 6729783719235132,
                       6729783719235152,
                       6729783719235159, 6729783719235169, 6729783719235171,
                       6729783719235201,
                       6729783719235266, 6729783719235271, 6729783719235272,
                       6729783719235285,
                       6729783719235286, 6729783719235287, 6729783719235288,
                       6729783719235289,
                       6729783719235533, 6729783719236798, 6729783719240567,
                       6729783719240568,
                       6729783719235534, 6729783719237333, 6729783719236294,
                       6729783719236292,
                       6729783719235362, 6729783719236670, 6729783719237286,
                       6729783719236304,
                       6729783719236888, 6729783719237380, 6729783719235454,
                       6729783719240674,
                       6729783719237883, 6729783719235617, 6729783719236799,
                       6729783719237299,
                       6729783719235537, 6729783719236438, 6729783719237884,
                       6729783719236397,
                       6729783719237206, 6729783719237322, 6729783719237008,
                       6729783719236122,
                       6729783719235016, 6729783719235945, 6729783719238168,
                       6729783719236909,
                       6729783719235944, 6729783719237422, 6729783719236660,
                       6729783719236659,
                       6729783719236031, 6729783719237105, 6729783719237077,
                       6729783719237707,
                       6729783719236723, 6729783719236806, 6729783719235532,
                       6729783719237231,
                       6729783719237100, 6729783719236578, 6729783719237666,
                       6729783719235453,
                       6729783719238180, 6729783719236684, 6729783719236403,
                       6729783719240838,
                       6729783719235543, 6729783719236686, 6729783719237127,
                       6729783719237176,
                       6729783719236514, 6729783719235768, 6729783719235535,
                       6729783719236662,
                       6729783719240897, 6729783719236016, 6729783719239599,
                       6729783719235618,
                       6729783719238169, 6729783719237755, 6729783719235363,
                       6729783719235536,
                       6729783719236293, 6729783719237327, 6729783719237328,
                       6729783719237381,
                       6729783719237505, 6729783719238317, 6729783719238325,
                       6729783719238333,
                       6729783719238343, 6729783719237679, 6729783719237678,
                       6729783719238511,
                       6729783719234828, 6729783719238567, 6729783719238580,
                       6729783719237578,
                       6729783719238711, 6729783719235351, 6729783719238743,
                       6729783719238792,
                       6729783719238800, 6729783719238915, 6729783719238931,
                       6729783719236859,
                       6729783719239001, 6729783719239190, 6729783719239514,
                       6729783719239379,
                       6729783719239706, 6729783719237321, 6729783719242268,
                       6729783719237299,
                       6729783719234855, 6729783719238404, 6729783719234797,
                       6729783719234799,
                       6729783719234800, 6729783719234679, 6729783719235269,
                       6729783719235270,
                       6729783719235615, 6729783719241071, 6729783719237175,
                       6729783719234717,
                       6729783719240175, 6729783719240177, 6729783719235544,
                       6729783719240380,
                       6729783719234527, 6729783719240889, 6729783719235015]
        for ar in autorefills:
            autorefill = AutoRefill.objects.get(id=ar)
            if autorefill.customer.charge_getaway != Customer.REDFIN:
                if not autorefill.enabled:
                    print autorefill.customer.charge_getaway, autorefill.enabled
                    # autorefill.enabled = True
                    # autorefill.save()
                else:
                    print autorefill.customer.charge_getaway, autorefill.enabled
            else:
                print autorefill.customer.charge_getaway, autorefill.enabled
        print 'DONE'