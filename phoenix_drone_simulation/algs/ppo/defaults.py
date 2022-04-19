"""
    Define default parameters for Proximal Policy Optimization (PPO) algorithm.
"""


def defaults():
    return dict(
        actor='mlp',
        ac_kwargs={
            'pi': {'hidden_sizes': (50, 50),
                   'activation': 'relu'},
            'val': {'hidden_sizes': (64, 64),
                    'activation': 'tanh'}
        },
        adv_estimation_method='gae',
        epochs=300,  # 3.2M steps
        gamma=0.99,
        steps_per_epoch=32 * 1000
    )


def locomotion():
    """Default hyper-parameters for Bullet's locomotion environments."""
    params = defaults()
    params['epochs'] = 312
    params['max_ep_len'] = 1000
    params['pi_lr'] = 3e-4  # default choice is Adam
    params['steps_per_epoch'] = 32 * 1000
    params['vf_lr'] = 3e-4  # default choice is Adam
    return params


# Hack to circumvent kwarg errors with the official PyBullet Envs
def gym_locomotion_envs():
    params = locomotion()
    return params


def gym_manipulator_envs():
    """Default hyper-parameters for Bullet's manipulation environments."""
    params = defaults()
    params['epochs'] = 312
    params['max_ep_len'] = 150
    params['pi_lr'] = 3e-4  # default choice is Adam
    params['steps_per_epoch'] = 32 * 1000
    params['vf_lr'] = 3e-4  # default choice is Adam
    return params
