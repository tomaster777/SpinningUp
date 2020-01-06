class Agent:
    def __init__(
        self, action_dim, observation_dim, action_space_type, observation_space_type
    ):
        self.action_dim = action_dim
        self.observation_dim = observation_dim
        self.action_space_type = action_space_type
        self.observation_space_type = observation_space_type

    def act(self, observation):
        """return an action from the action space
        
        Arguments:
            observation {observation} -- env observation
        """
        raise NotImplementedError()

    def learn(self, observation, action, reward, new_observation):
        """learn from action
        
        Arguments:
            observation {observation} -- env observation
            action {action} -- action agent took
            reward {float} -- reward given after action in observation
            new_observation {observation} -- env observation following agent action
        """
        raise NotImplementedError()
