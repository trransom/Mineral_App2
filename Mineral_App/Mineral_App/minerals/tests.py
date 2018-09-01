from django.test import TestCase
from django.urls import reverse
from .models import Mineral

class CourseViewsTests(TestCase):
	def setUp(self):
		self.mineral = Mineral.objects.create(
			name = "Aegirine",
			img_filename = "Aegirine.jpg",
			img_caption = "Monoclinic Crystal Of Aegirine With Orthoclase, From Mount Malosa, Zomba District, Malawi (Size: 85 Mm X 83 Mm; 235 G)",
			category = "Silicate, Pyroxene",
			formula = "<Sub>231</Sub>.<Sub>00</Sub>",
			strunz_class = "09.Da.25",
			color = "Dark Green, Greenish Black",
			crystal_sys = "Monoclinic Prismatic",
			unit_cell = "A = 9.658 Å, B = 8.795 Å, C = 5.294 Å, Β = 107.42°; Z=4",
			crystal_sym = "",
			cleavage = "Good On {110}, (110) ^ (110) ≈87°; Parting On {100}",
			mohs = "6",
			luster = "Vitreous To Slightly Resinous",
			streak = "Yellowish-Grey",
			diaphaneity = "Translucent To Opaque",
			optical_prop = "Biaxial(-)",
			refractive_inx = "Nα = 1.720 - 1.778 Nβ = 1.740 - 1.819 Nγ = 1.757 - 1.839",
			crystal_habit = "",
			spec_gravity = ""
		)
		self.mineral2 = Mineral.objects.create(
			name = "Penroseite",
			img_filename = "Penroseite.jpg",
			img_caption = "Penroseite From Pakajake Canyon, Chayanta Province, Potosí Department, Bolivia",
			category = "Selenide, Pyrite Group",
			formula = "(Ni,Co,Cu)Se<Sub>2</Sub>",
			strunz_class = "02.Eb.05a",
			color = "Steel Gray",
			crystal_sys = "Isometric Diploidal 2/M3",
			unit_cell = "",
			crystal_sym = "",
			cleavage = "{001} Perfect, {011} Distinct",
			mohs = "2.5-3",
			luster = "Metallic",
			streak = "Black",
			diaphaneity = "Opaque",
			optical_prop = "",
			refractive_inx = "",
			crystal_habit = "",
			spec_gravity = ""
		)
		
	def test_index_view(self):
		'''Tests the index display of the minerals.'''
		resp = self.client.get(reverse('minerals:index', kwargs={'letter': 'A'}))
		self.assertEqual(resp.status_code, 200)
		self.assertIn(self.mineral, resp.context['minerals'])
		self.assertTemplateUsed(resp, 'minerals/index.html')
		
	def test_mineral_view(self):
		'''Tests the individual mineral display.'''
		resp = self.client.get(reverse('minerals:detail', kwargs={'pk': self.mineral.pk}))
		self.assertEqual(resp.status_code, 200)
		self.assertEqual(self.mineral, resp.context['mineral'])
		
	def test_search_results(self):
		'''Tests the detail view of a selected mineral.'''
		resp = self.client.get(reverse('minerals:search_results'), {'q': 'Aegirine'})#, kwargs={'q': 'Aegirine'}
		self.assertEqual(resp.status_code, 200)
		self.assertIn(self.mineral, resp.context['minerals'])
		
	def test_group_view(self):
		'''Tests the view showing groups of minerals.'''
		resp = self.client.get(reverse('minerals:group_view', kwargs={'group': 'silicate'}))
		self.assertEqual(resp.status_code, 200)
		self.assertIn(self.mineral, resp.context['minerals'])