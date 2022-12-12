from FunkcePole import FunkcePole


class TestFunkcePole():
    def test_minimum(self):
        assert FunkcePole.minimum([8, -8, 2]) == (-8, 2)




    class TestSort():

        def test_bubble_sort(self):
            assert FunkcePole.Sort.bubble_sort([8, -8, 2]) == [-8, 2, 8]

        def test_insertion_sort(self):
            assert FunkcePole.Sort.insertion_sort([8, -8, 2]) == [-8, 2, 8]

        def test_selection_sort(self):
            assert FunkcePole.Sort.selection_sort([8, -8, 2]) == [-8, 2, 8]
