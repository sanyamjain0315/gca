if __name__=="__main__":
  import numpy as np
  import matplotlib.pyplot as plt

  npz_file = np.load('gca-data/data/shapenet_sdf/chair/test/cc03a89a98cd2660c423490470c47d79.npz')

  # Extract arrays
  surface = npz_file['surface']
  partial = npz_file['partial']

  # Setup figure
  fig = plt.figure(figsize=(12, 6))

  # Plot surface points
  ax1 = fig.add_subplot(121, projection='3d')
  ax1.scatter(surface[:, 0], surface[:, 1], surface[:, 2], c='blue', s=0.5)
  ax1.set_title('Surface Points')
  ax1.set_xlabel('X')
  ax1.set_ylabel('Y')
  ax1.set_zlabel('Z')
  ax1.set_box_aspect([1,1,1])

  # Plot partial points
  ax2 = fig.add_subplot(122, projection='3d')
  ax2.scatter(partial[:, 0], partial[:, 1], partial[:, 2], c='red', s=5)
  ax2.set_title('Partial Point Cloud')
  ax2.set_xlabel('X')
  ax2.set_ylabel('Y')
  ax2.set_zlabel('Z')
  ax2.set_box_aspect([1,1,1])

  plt.tight_layout()
  plt.show()
  plt.savefig('fig.png')
