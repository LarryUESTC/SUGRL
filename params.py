import argparse


def parse_args(dataset):
    parser = argparse.ArgumentParser()
    if dataset == 'acm':
        parser.add_argument('--cfg', type=int, default=[512, 128], help='hidden dimension')
        parser.add_argument('--dataset', nargs='?', default='acm')
        parser.add_argument('--sc', type=float, default=3.0, help='GCN self connection')
        parser.add_argument('--sparse', type=bool, default=False, help='sparse adjacency matrix')
        parser.add_argument('--nb_epochs', type=int, default=400, help='the number of epochs')
        parser.add_argument('--lr', type=float, default=0.001, help='learning rate')
        parser.add_argument('--gpu_num', type=int, default=0, help='the id of gpu to use')
        parser.add_argument('--seed', type=int, default=2021, help='the seed to use')
        parser.add_argument('--test_epo', type=int, default=100, help='test_epo')
        parser.add_argument('--test_lr', type=int, default=0.01, help='test_lr')
        parser.add_argument('--save_root', type=str, default="./saved_model", help='root for saving the model')
        parser.add_argument('--neg_num', type=int, default=6, help='the number of negtives')
        parser.add_argument('--margin1', type=float, default=0.6, help='')
        parser.add_argument('--margin2', type=float, default=0.1, help='')
        parser.add_argument('--w_s', type=float, default=2, help='weight of loss L_s')
        parser.add_argument('--w_c', type=float, default=2, help='weight of loss L_c')
        parser.add_argument('--w_u', type=float, default=10, help='weight of loss L_u')
    elif dataset == 'dblp':
        parser.add_argument('--cfg', type=int, default=[512, 128], help='hidden dimension')
        parser.add_argument('--dataset', nargs='?', default='dblp')
        parser.add_argument('--sc', type=float, default=3.0, help='GCN self connection')
        parser.add_argument('--sparse', type=bool, default=False, help='sparse adjacency matrix')
        parser.add_argument('--nb_epochs', type=int, default=3500, help='the number of epochs')
        parser.add_argument('--lr', type=float, default=0.0001, help='learning rate')
        parser.add_argument('--gpu_num', type=int, default=0, help='the id of gpu to use')
        parser.add_argument('--seed', type=int, default=2021, help='the seed to use')
        parser.add_argument('--test_epo', type=int, default=200, help='test_epo')
        parser.add_argument('--test_lr', type=int, default=0.01, help='test_lr')
        parser.add_argument('--save_root', type=str, default="./saved_model", help='root for saving the model')
        parser.add_argument('--neg_num', type=int, default=8, help='the number of negtives')
        parser.add_argument('--margin1', type=float, default=0.9, help='')
        parser.add_argument('--margin2', type=float, default=0.1, help='')
        parser.add_argument('--w_s', type=float, default=0.7, help='weight of loss L_s')
        parser.add_argument('--w_c', type=float, default=9.0, help='weight of loss L_c')
        parser.add_argument('--w_u', type=float, default=0.4, help='weight of loss L_u')

    elif dataset == 'imdb':
        parser.add_argument('--cfg', type=int, default=[512, 256], help='hidden dimension')
        parser.add_argument('--dataset', nargs='?', default='imdb')
        parser.add_argument('--sc', type=float, default=3.0, help='GCN self connection')
        parser.add_argument('--sparse', type=bool, default=False, help='sparse adjacency matrix')
        parser.add_argument('--nb_epochs', type=int, default=600, help='the number of epochs')
        parser.add_argument('--lr', type=float, default=0.0005, help='learning rate')
        parser.add_argument('--gpu_num', type=int, default=0, help='the id of gpu to use')
        parser.add_argument('--seed', type=int, default=2021, help='the seed to use')
        parser.add_argument('--test_epo', type=int, default=200, help='test_epo')
        parser.add_argument('--test_lr', type=int, default=0.01, help='test_lr')
        parser.add_argument('--save_root', type=str, default="./saved_model", help='root for saving the model')
        parser.add_argument('--neg_num', type=int, default=4, help='the number of negtives')
        parser.add_argument('--margin1', type=float, default=1.0, help='')
        parser.add_argument('--margin2', type=float, default=1.0, help='')
        parser.add_argument('--w_s', type=float, default=9, help='weight of loss L_s')
        parser.add_argument('--w_c', type=float, default=2.5, help='weight of loss L_c')
        parser.add_argument('--w_u', type=float, default=2.5, help='weight of loss L_u')

    elif dataset == 'freebase':
        parser = argparse.ArgumentParser()
        parser.add_argument('--cfg', type=int, default=[256, 256], help='hidden dimension')
        parser.add_argument('--dataset', nargs='?', default='freebase')
        parser.add_argument('--sc', type=float, default=3.0, help='GCN self connection')
        parser.add_argument('--sparse', type=bool, default=False, help='sparse adjacency matrix')
        parser.add_argument('--nb_epochs', type=int, default=1000, help='the number of epochs')
        parser.add_argument('--lr', type=float, default=0.001, help='learning rate')
        parser.add_argument('--gpu_num', type=int, default=0, help='the id of gpu to use')
        parser.add_argument('--seed', type=int, default=2021, help='the seed to use')
        parser.add_argument('--test_epo', type=int, default=50, help='test_epo')
        parser.add_argument('--test_lr', type=int, default=0.01, help='test_lr')
        parser.add_argument('--save_root', type=str, default="./saved_model", help='root for saving the model')
        parser.add_argument('--neg_num', type=int, default=14, help='the number of negtives')
        parser.add_argument('--margin1', type=float, default=0.55, help='')
        parser.add_argument('--margin2', type=float, default=0.1, help='')
        parser.add_argument('--w_s', type=float, default=7, help='weight of loss L_s')
        parser.add_argument('--w_c', type=float, default=2, help='weight of loss L_c')
        parser.add_argument('--w_u', type=float, default=0.1, help='weight of loss L_u')

    else:
        raise ValueError("no such dataset")
    return parser.parse_known_args()


def printConfig(args):
    arg2value = {}
    for arg in vars(args):
        arg2value[arg] = getattr(args, arg)
    print(arg2value)
