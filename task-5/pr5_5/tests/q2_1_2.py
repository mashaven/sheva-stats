test = {
  'name': 'Question 2.1.2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure you can use any two songs
          >>> correct_dis = 0.0432734877749
          >>> dis = distance_two_features("Lookin' for Love", "Insane In The Brain", "like", "love")
          >>> np.isclose(dis, correct_dis)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Make sure you can use any two features
          >>> correct_dis = 0.0338289443246
          >>> dis = distance_two_features("In Your Eyes", "Sangria Wine", "the", "of")
          >>> np.isclose(dis, correct_dis)
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
