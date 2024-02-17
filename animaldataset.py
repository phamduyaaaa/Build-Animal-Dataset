from torch.utils.data import Dataset
import os
import cv2

class AnimalsDataset(Dataset):
    def __init__(self, root, test_or_train):
        list_label = ['butterfly', 'cat', 'chicken', 'cow', 'dog', 'elephant', 'horse', 'sheep', 'spider', 'squirrel']
        self.all_labels = []
        self.all_img_paths = []
        if test_or_train == "test":
            for label in list_label:
                data_file = os.path.join(root, label)
                for filename in os.listdir(data_file):
                    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
                        img_path = os.path.join(data_file, filename)
                        self.all_img_paths.append(img_path)
                        self.all_labels.append(label)
        elif test_or_train == "train":
            for label in list_label:
                data_file = os.path.join(root, label)
                for filename in os.listdir(data_file):
                    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
                        img_path = os.path.join(data_file, filename)
                        self.all_img_paths.append(img_path)
                        self.all_labels.append(label)
    def __len__(self):
        return len(self.all_labels)
    def __getitem__(self, index):
        img_path = self.all_img_paths[index]
        image = cv2.imread(img_path)
        label = self.all_labels[index]
        print(image.shape)
        return image, label

if __name__ == '__main__':
    train_dataset = AnimalsDataset(root="animals_v2\\animals\\test", test_or_train="test")
    image,label = train_dataset[2579]
    print(train_dataset.__len__())
    cv2.imshow(label,image)
    cv2.waitKey(0)
