import unittest
from panml.search import VectorEngine

class TestVectorEngine(unittest.TestCase):
    '''
    Run tests on VecterEngine class in search.py
    '''
    # Test case: handle invalid source input
    print('Setup test_faiss_hf_invalid_source_input')
    def test_faiss_hf_invalid_source_input(self):
        # test invalid source as int
        with self.assertRaises(ValueError):
            m = VectorEngine(model=None, source=1)
        # test invalid source as float
        with self.assertRaises(ValueError):
            m = VectorEngine(model=None, source=0.2)
        # test invalid source as non accepted str
        with self.assertRaises(ValueError):
            m = VectorEngine(model=None, source='faiss1')

    # Test case: handle invalid model input
    print('Setup test_faiss_hf_invalid_model_input')
    def test_faiss_hf_invalid_model_input(self):
        # test invalid model as int
        with self.assertRaises(ValueError):
            m = VectorEngine(model=1, source='faiss')
        # test invalid model as float
        with self.assertRaises(ValueError):
            m = VectorEngine(model=0.2, source='faiss')
        # test invalid model as non accepted str
        with self.assertRaises(ValueError):
            m = VectorEngine(model='distilbert-base-nli-stsb-mean-tokens1', source='faiss')

    # Test case: handle invalid corpus input
    print('Setup test_faiss_hf_invalid_corpus_input_storage')
    def test_faiss_hf_invalid_corpus_input_storage(self):
        # test invalid corpus store input type
        with self.assertRaises(TypeError):
            m = VectorEngine(model='distilbert-base-nli-stsb-mean-tokens', source='faiss')
            TEST_CORPUS = 1
            m.store(TEST_CORPUS)

        # test invalid corpus store input type
        with self.assertRaises(TypeError):
            m = VectorEngine(model='distilbert-base-nli-stsb-mean-tokens', source='faiss')
            TEST_CORPUS = 0.2
            m.store(TEST_CORPUS)

        # test invalid corpus store input type - None
        with self.assertRaises(TypeError):
            m = VectorEngine(model='distilbert-base-nli-stsb-mean-tokens', source='faiss')
            TEST_CORPUS = None
            m.store(TEST_CORPUS)

        # test invalid corpus store input value - empty
        with self.assertRaises(ValueError):
            m = VectorEngine(model='distilbert-base-nli-stsb-mean-tokens', source='faiss')
            TEST_CORPUS = []
            m.store(TEST_CORPUS)

    # Test case: handle invalid model input
    print('Setup test_faiss_hf_invalid_corpus_input_query')
    def test_faiss_hf_invalid_corpus_input_query(self):
        # test invalid corpus query input type
        with self.assertRaises(TypeError):
            m = VectorEngine(model='distilbert-base-nli-stsb-mean-tokens', source='faiss')
            TEST_CORPUS = [
                'The quick brown fox jumps over the lazy dog', 
                'The quick brown rabbit jumps over the lazy dog', 
                'The quick brown rabbit jumps over the lazy cat', 
                'The quick brown cat jumps over the lazy dog', 
                'The quick brown cat jumps over the lazy rabbit', 
                'The quick brown cat jumps over the lazy fox', 
                'The quick brown cat is lazy', 
                'The quick brown fox is lazy', 
                'The slow brown dog is lazy', 
                'The slow white rabbit is lazy',
            ]
            TEST_SAMPLE = 1
            m.store(TEST_CORPUS)
            output = m.search(TEST_SAMPLE, 3)

        # test invalid corpus query input type
        with self.assertRaises(TypeError):
            m = VectorEngine(model='distilbert-base-nli-stsb-mean-tokens', source='faiss')
            TEST_CORPUS = [
                'The quick brown fox jumps over the lazy dog', 
                'The quick brown rabbit jumps over the lazy dog', 
                'The quick brown rabbit jumps over the lazy cat', 
                'The quick brown cat jumps over the lazy dog', 
                'The quick brown cat jumps over the lazy rabbit', 
                'The quick brown cat jumps over the lazy fox', 
                'The quick brown cat is lazy', 
                'The quick brown fox is lazy', 
                'The slow brown dog is lazy', 
                'The slow white rabbit is lazy',
            ]
            TEST_SAMPLE = 0.2
            m.store(TEST_CORPUS)
            output = m.search(TEST_SAMPLE, 3)

        # test invalid corpus query input type - None
        with self.assertRaises(TypeError):
            m = VectorEngine(model='distilbert-base-nli-stsb-mean-tokens', source='faiss')
            TEST_CORPUS = [
                'The quick brown fox jumps over the lazy dog', 
                'The quick brown rabbit jumps over the lazy dog', 
                'The quick brown rabbit jumps over the lazy cat', 
                'The quick brown cat jumps over the lazy dog', 
                'The quick brown cat jumps over the lazy rabbit', 
                'The quick brown cat jumps over the lazy fox', 
                'The quick brown cat is lazy', 
                'The quick brown fox is lazy', 
                'The slow brown dog is lazy', 
                'The slow white rabbit is lazy',
            ]
            TEST_SAMPLE = None
            m.store(TEST_CORPUS)
            output = m.search(TEST_SAMPLE, 3)

        # test invalid corpus query input type
        with self.assertRaises(TypeError):
            m = VectorEngine(model='distilbert-base-nli-stsb-mean-tokens', source='faiss')
            TEST_CORPUS = [
                'The quick brown fox jumps over the lazy dog', 
                'The quick brown rabbit jumps over the lazy dog', 
                'The quick brown rabbit jumps over the lazy cat', 
                'The quick brown cat jumps over the lazy dog', 
                'The quick brown cat jumps over the lazy rabbit', 
                'The quick brown cat jumps over the lazy fox', 
                'The quick brown cat is lazy', 
                'The quick brown fox is lazy', 
                'The slow brown dog is lazy', 
                'The slow white rabbit is lazy',
            ]
            TEST_SAMPLE = []
            m.store(TEST_CORPUS)
            output = m.search(TEST_SAMPLE, 3)

    # Test case: validate FAISS vector search functionality
    print('Setup test_faiss_hf_vector_search')
    def test_faiss_hf_vector_search(self):
        # test sample input
        TEST_CORPUS = [
            'The quick brown fox jumps over the lazy dog', 
            'The quick brown rabbit jumps over the lazy dog', 
            'The quick brown rabbit jumps over the lazy cat', 
            'The quick brown cat jumps over the lazy dog', 
            'The quick brown cat jumps over the lazy rabbit', 
            'The quick brown cat jumps over the lazy fox', 
            'The quick brown cat is lazy', 
            'The quick brown fox is lazy', 
            'The slow brown dog is lazy', 
            'The slow white rabbit is lazy',
        ]
        TEST_SAMPLES = [
            {
                'text': 'white rabbit',
                'k': 3,
                'expected_output': [
                    'The slow white rabbit is lazy',
                    'The quick brown rabbit jumps over the lazy dog',
                    'The quick brown rabbit jumps over the lazy cat'
                ],
            },
        ]
        # Run vector search validation
        m = VectorEngine(source='faiss')
        m.store(TEST_CORPUS)
        for sample in TEST_SAMPLES:
            output = m.search(sample['text'], sample['k']) # get test output
            self.assertEqual(output, sample['expected_output'], 'FAISS vector search output is not as expected, review may be required.') # check test output against expected output

    # Test case: validate FAISS vector search missing OpenAI key
    print('Setup test_faiss_missing_openai_key')
    def test_faiss_missing_openai_key(self):
        # test no openai api key provided
        with self.assertRaises(ValueError):
            m = VectorEngine(model='text-davinci-002', source='faiss')

    # Test case: validate FAISS vector store save functionality
    print('Setup test_faiss_invalid_save_name_vector_store')
    def test_faiss_invalid_save_name_vector_store(self):
        # test invalid save name input type
        with self.assertRaises(TypeError):
            # test sample input
            TEST_CORPUS = [
                'The quick brown fox jumps over the lazy dog', 
                'The quick brown rabbit jumps over the lazy dog', 
                'The quick brown rabbit jumps over the lazy cat', 
                'The quick brown cat jumps over the lazy dog', 
                'The quick brown cat jumps over the lazy rabbit', 
                'The quick brown cat jumps over the lazy fox', 
                'The quick brown cat is lazy', 
                'The quick brown fox is lazy', 
                'The slow brown dog is lazy', 
                'The slow white rabbit is lazy',
            ]

            # Run vector search validation
            m = VectorEngine(source='faiss')
            m.store(TEST_CORPUS, save_name=1)

    # Test case: validate FAISS vector store load vectors functionality
    print('Setup test_faiss_invalid_load_vectors_dir')
    def test_faiss_invalid_load_vectors_dir(self):
        # test invalid vectors dir input type
        with self.assertRaises(TypeError):
            # Run vector search validation
            m = VectorEngine(source='faiss')
            m.load(vectors_dir=1, corpus_dir='corpus.pkl')

        with self.assertRaises(TypeError):
            # Run vector search validation
            m = VectorEngine(source='faiss')
            m.load(vectors_dir=None, corpus_dir='corpus.pkl')

        # test invalid vectors dir input name
        with self.assertRaises(ValueError):
            # Run vector search validation
            m = VectorEngine(source='faiss')
            m.load(vectors_dir='vectors', corpus_dir='corpus.pkl')

    # Test case: validate FAISS vector store load corpus functionality
    print('Setup test_faiss_invalid_load_corpus_dir')
    def test_faiss_invalid_load_corpus_dir(self):
        # test invalid load corpus dir type
        with self.assertRaises(TypeError):
            # Run vector search validation
            m = VectorEngine(source='faiss')
            m.load(vectors_dir='vectors.faiss', corpus_dir=1)

        with self.assertRaises(TypeError):
            # Run vector search validation
            m = VectorEngine(source='faiss')
            m.load(vectors_dir='vectors.faiss', corpus_dir=None)

        # test invalid load corpus dir input name
        with self.assertRaises(ValueError):
            # Run vector search validation
            m = VectorEngine(source='faiss')
            m.load(vectors_dir='vectors.faiss', corpus_dir='corpus')