test = {
  'name': 'Question 1.2.1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from collections import Counter
          >>> g = train_lyrics.column('Genre')
          >>> classify(test_20.row(0), train_20, g, 5) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(0), train_20))[:5])).most_common(1)[0][0]
          True
          >>> classify(test_20.row(0), train_20, g, 11) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(0), train_20))[:11])).most_common(1)[0][0]
          True
          >>> classify(test_20.row(1), train_20, g, 5) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(1), train_20))[:5])).most_common(1)[0][0]
          True
          >>> classify(test_20.row(1), train_20, g, 11) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(1), train_20))[:11])).most_common(1)[0][0]
          True
          >>> classify(test_20.row(2), train_20, g, 5) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(2), train_20))[:5])).most_common(1)[0][0]
          True
          >>> classify(test_20.row(2), train_20, g, 11) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(2), train_20))[:11])).most_common(1)[0][0]
          True
          >>> classify(test_20.row(3), train_20, g, 5) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(3), train_20))[:5])).most_common(1)[0][0]
          True
          >>> classify(test_20.row(3), train_20, g, 11) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(3), train_20))[:11])).most_common(1)[0][0]
          True
          >>> classify(test_20.row(4), train_20, g, 5) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(4), train_20))[:5])).most_common(1)[0][0]
          True
          >>> classify(test_20.row(4), train_20, g, 11) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(4), train_20))[:11])).most_common(1)[0][0]
          True
          >>> classify(test_20.row(5), train_20, g, 5) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(5), train_20))[:5])).most_common(1)[0][0]
          True
          >>> classify(test_20.row(5), train_20, g, 11) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(5), train_20))[:11])).most_common(1)[0][0]
          True
          >>> classify(test_20.row(6), train_20, g, 5) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(6), train_20))[:5])).most_common(1)[0][0]
          True
          >>> classify(test_20.row(6), train_20, g, 11) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(6), train_20))[:11])).most_common(1)[0][0]
          True
          >>> classify(test_20.row(7), train_20, g, 5) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(7), train_20))[:5])).most_common(1)[0][0]
          True
          >>> classify(test_20.row(7), train_20, g, 11) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(7), train_20))[:11])).most_common(1)[0][0]
          True
          >>> classify(test_20.row(8), train_20, g, 5) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(8), train_20))[:5])).most_common(1)[0][0]
          True
          >>> classify(test_20.row(8), train_20, g, 11) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(8), train_20))[:11])).most_common(1)[0][0]
          True
          >>> classify(test_20.row(9), train_20, g, 5) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(9), train_20))[:5])).most_common(1)[0][0]
          True
          >>> classify(test_20.row(9), train_20, g, 11) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(9), train_20))[:11])).most_common(1)[0][0]
          True
          >>> classify(test_20.row(10), train_20, g, 5) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(10), train_20))[:5])).most_common(1)[0][0]
          True
          >>> classify(test_20.row(10), train_20, g, 11) == Counter(np.take(g, np.argsort(fast_distances(test_20.row(10), train_20))[:11])).most_common(1)[0][0]
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
