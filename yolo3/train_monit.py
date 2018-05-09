import matplotlib.pyplot as plt

print("import finish")
class TrainMonitorTools():
    def __init__(self):
        print("train process tool")
    def visualizeTrain(self, history):
        # plot code from tutorial: https://machinelearningmastery.com/display-deep-learning-model-training-history-in-keras/
        print(history.history.keys())  # dict_keys(['val_acc', 'acc', 'loss', 'val_loss'])
        plt.close('all')
        # summarize history for accuracy
        plt.plot(history.history['acc'])
        plt.plot(history.history['val_acc'])
        plt.title('model accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.savefig('../visualize/acc.jpg')
        # plt.show()
        # summarize history for loss
        plt.close('all')
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        # plt.show()
        plt.savefig('../visualize/loss.jpg')

        # loss = history.history['loss']
        # print("loss", loss)
        # save model
        # self.lenetModel.save(self.train_model_path)
        # todo: include validation set , early stopping when validation accuracy and training accuracy close
        # https://chrisalbon.com/deep_learning/keras/neural_network_early_stopping/
