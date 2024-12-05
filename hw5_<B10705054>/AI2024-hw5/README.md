### Environment Setup
    Install Necessary Packages
    Create a new conda environment with Python 3.11:
   **conda create -n hw5 python=3.11 -y**
    Activate the conda environment:
    **conda activate hw5**
    Install the required packages from requirements.txt:
    **pip install -r requirements.txt**
### Training
    Finish editing both pacman.py and rl_algorithm.py, especially the areas marked with "*** YOUR CODE HERE ***". You may also adjust default parameters in the scripts if necessary.
    Run the Training Script
    To start the training process, execute the following command:
   **python pacman.py**
    This command will initiate the training of the DQN agent in the MsPacman environment. The trained model will be saved to the specified directory.
### Evaluation
    Ensure sodel is Trained
    Before running the evaluation, ensure that you have a trained model. If you haven't trained the model yet, follow the training steps above.
    Run the Evaluation Script
    To evaluate the trained model, execute the following command:
   **python pacman.py --eval --eval_model_path <path_to_trained_model>**
   **python3 pacman.py --eval --eval_model_path <path_to_trained_model>**
    my personal computer only works withe the second command line
    Replace <path_to_trained_model> with the actual path to your trained model file, e.g., ./submissions/pacman_dqn.pt.
    Evaluation Results
    The evaluation results will be printed to the console, displaying the average score of the agent over multiple games.
