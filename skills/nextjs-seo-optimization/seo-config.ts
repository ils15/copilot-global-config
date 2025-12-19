# Next.js SEO Config Templates

```typescript
// seo-config.ts
export const seoConfig = {
  siteName: 'OfertaChina',
  defaultTitle: 'OfertaChina - Melhores Cupons e Ofertas',
  defaultDescription: 'Encontre as melhores ofertas da AliExpress e plataformas chinesas. Cupons exclusivos, frete grátis e cashback.',
  url: 'https://ofertachina.com',
  twitterHandle: '@ofertachina',
  email: 'contato@ofertachina.com',
  
  // Image sizes
  ogImageWidth: 1200,
  ogImageHeight: 630,
  
  // Locales
  locales: ['pt-BR', 'pt', 'en'],
  defaultLocale: 'pt-BR',
  
  // Categories for products
  categories: [
    'eletrônicos',
    'moda',
    'casa',
    'games',
    'livros',
    'esportes',
    'saúde'
  ]
}

export function generateMetadataBase() {
  return new URL(seoConfig.url)
}

export function generateOpenGraph(
  title: string,
  description: string,
  imageUrl: string = '/og-default.png',
  type: 'website' | 'product' | 'article' = 'website'
) {
  return {
    type,
    locale: seoConfig.defaultLocale,
    url: seoConfig.url,
    siteName: seoConfig.siteName,
    title,
    description,
    images: [
      {
        url: imageUrl,
        width: seoConfig.ogImageWidth,
        height: seoConfig.ogImageHeight,
        alt: title
      }
    ]
  }
}

export function generateTwitterCard(
  title: string,
  description: string,
  imageUrl: string = '/og-default.png'
) {
  return {
    card: 'summary_large_image',
    title,
    description,
    images: [imageUrl],
    creator: seoConfig.twitterHandle
  }
}
```

## Usage

```typescript
import { seoConfig, generateOpenGraph, generateTwitterCard } from '@/config/seo'

export const metadata: Metadata = {
  title: `Product Title | ${seoConfig.siteName}`,
  description: 'Product description',
  metadataBase: generateMetadataBase(),
  openGraph: generateOpenGraph('Product Title', 'Description', '/image.png', 'product'),
  twitter: generateTwitterCard('Product Title', 'Description', '/image.png'),
}
```
