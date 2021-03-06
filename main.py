""" 
Image Variational Autoencoding
"""

import sys
import os
import argparse

from image_vae import ImageVAE

parser = argparse.ArgumentParser(description='')

parser.add_argument('--data_dir',       type=str,   default='data',     help='input data directory (in train subfolder)')
parser.add_argument('--save_dir',       type=str,   default='save',     help='save directory')
parser.add_argument('--phase',          type=str,   default='train',    help='train or load')
parser.add_argument('--checkpoint',     type=str,   default='NA',       help='checkpoint weight file')

parser.add_argument('--image_size',     type=int,   default=64,         help='image size')
parser.add_argument('--image_channel',  type=int,   default=3,          help='image channels')
parser.add_argument('--image_res',      type=int,   default=8,          help='image resolution (8 or 16)')

parser.add_argument('--latent_dim',     type=int,   default=2,          help='latent dimension')
parser.add_argument('--inter_dim',      type=int,   default=64,         help='intermediate dimension')
parser.add_argument('--num_conv',       type=int,   default=3,          help='number of convolutions')
parser.add_argument('--batch_size',     type=int,   default=32,         help='batch size')
parser.add_argument('--epochs',         type=int,   default=2,          help='training epochs')
parser.add_argument('--nfilters',       type=int,   default=64,         help='num convolution filters')
parser.add_argument('--learn_rate',     type=float, default=0.001,      help='learning rate')
parser.add_argument('--epsilon_std',    type=float, default=1.0,        help='epsilon width')
parser.add_argument('--latent_samp',    type=int,   default=10,         help='number of latent samples')
parser.add_argument('--num_save',       type=int,   default=8,          help='number of reconstructed images to save')
parser.add_argument('--verbose',        type=int,   default=2,          help='1=verbose, 2=quiet')

parser.add_argument('--steps_per_epoch',    type=int,   default=0,      help='steps per epoch')

args = parser.parse_args()


def main():

    os.makedirs(args.save_dir, exist_ok=True)
    os.makedirs(os.path.join(args.save_dir, 'checkpoints'), exist_ok=True)
    os.makedirs(os.path.join(args.save_dir, 'latent_walk'), exist_ok=True)
    os.makedirs(os.path.join(args.save_dir, 'input'), exist_ok=True)
    os.makedirs(os.path.join(args.save_dir, 'reconstructed'), exist_ok=True)
        
    if args.phase == 'train':
        model = ImageVAE(args)
        model.train()

    if args.phase == 'load':
        if args.checkpoint == 'NA':
            sys.exit('No checkpoint file provided')
            
        model = ImageVAE(args)
        model.vae.load_weights(args.checkpoint)
        model.train()
        
    
if __name__ == '__main__':
    main()
