"""实验 1：用 FrozenLake 熟悉 Gymnasium 的交互接口。"""

import gymnasium as gym
import numpy as np


def run_random_trajectory(env, max_steps=20, seed=None):
    """运行一条随机轨迹，并打印每一步的状态和回合总奖励。"""
    obs, info = env.reset(seed=seed)
    # reset 的种子控制环境随机性；动作空间需要单独设置种子。
    env.action_space.seed(seed)
    total_reward = 0.0
    print(f"初始状态: {obs}，信息: {info}")
    print(env.render())

    for step in range(max_steps):
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)
        total_reward += reward
        print(f"第 {step + 1} 步: 动作={action}, 状态={obs}, 奖励={reward}")
        print(env.render())
        if terminated or truncated:
            print(f"回合结束: terminated={terminated}, truncated={truncated}")
            break

    print(f"总奖励: {total_reward}\n")
    return total_reward


def main():
    # 确定性 4×4 地图：动作不会因为冰面打滑而偏离方向。
    env = gym.make("FrozenLake-v1", map_name="4x4", is_slippery=False, render_mode="ansi")
    try:
        print(f"状态空间: {env.observation_space} -> 共 {env.observation_space.n} 个状态")
        print(f"动作空间: {env.action_space} -> 共 {env.action_space.n} 个动作 (0=左, 1=下, 2=右, 3=上)")

        obs, info = env.reset(seed=42)
        print("\n初始地图：")
        print(env.render())

        # P[state][action] 的每项为 (概率, 下一状态, 奖励, 是否结束)。
        reward_map = np.zeros(env.observation_space.n)
        for transitions in env.unwrapped.P.values():
            for outcomes in transitions.values():
                for probability, next_state, reward, done in outcomes:
                    reward_map[next_state] = max(reward_map[next_state], reward)
        print("奖励地图（reshape 为 4×4）：")
        print(reward_map.reshape(4, 4))

        # 演示 reset 和 step；Notebook 中的 action 未定义，这里选择向右。
        obs, info = env.reset(seed=0)
        print(f"\n重置: obs={obs}, info={info}")
        action = 2
        obs, reward, terminated, truncated, info = env.step(action)
        print(f"step: action={action}, obs={obs}, reward={reward}, "
              f"terminated={terminated}, truncated={truncated}, info={info}")

        for i in range(3):
            print(f"\n=== 轨迹 {i + 1} ===")
            run_random_trajectory(env, max_steps=20, seed=100 + i)
    finally:
        env.close()


if __name__ == "__main__":
    main()

