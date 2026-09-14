import numpy as np
scores = np.array([94, 61, 77, 45, 90, 88, 59, 72])
medals = np.where(
    scores >= 90,
    'Gold',
    np.where(
        scores >= 75,
        'Silver',
        np.where(
            scores >= 60,
            'Bronze',
            'None'
        )
    )
)
print(medals)