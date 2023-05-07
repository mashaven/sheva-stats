test = {
  'name': 'Question 1.2.3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> classify(test_20.row(0), train_20, train_lyrics.column('Genre'), 5) == classify_one_argument(test_20.row(0))
          True
          >>> classify(test_20.row(1), train_20, train_lyrics.column('Genre'), 5) == classify_one_argument(test_20.row(1))
          True
          >>> classify(test_20.row(2), train_20, train_lyrics.column('Genre'), 5) == classify_one_argument(test_20.row(2))
          True
          >>> classify(test_20.row(3), train_20, train_lyrics.column('Genre'), 5) == classify_one_argument(test_20.row(3))
          True
          >>> classify(test_20.row(4), train_20, train_lyrics.column('Genre'), 5) == classify_one_argument(test_20.row(4))
          True
          >>> classify(test_20.row(5), train_20, train_lyrics.column('Genre'), 5) == classify_one_argument(test_20.row(5))
          True
          >>> classify(test_20.row(6), train_20, train_lyrics.column('Genre'), 5) == classify_one_argument(test_20.row(6))
          True
          >>> classify(test_20.row(7), train_20, train_lyrics.column('Genre'), 5) == classify_one_argument(test_20.row(7))
          True
          >>> classify(test_20.row(8), train_20, train_lyrics.column('Genre'), 5) == classify_one_argument(test_20.row(8))
          True
          >>> classify(test_20.row(9), train_20, train_lyrics.column('Genre'), 5) == classify_one_argument(test_20.row(9))
          True
          >>> classify(test_20.row(10), train_20, train_lyrics.column('Genre'), 5) == classify_one_argument(test_20.row(10))
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
